// ==== 1. CLASSIFY SEQUENCE ====
const form1 = document.getElementById("classify_form");
const circles = document.querySelectorAll(".progress-circle");
const numbers = document.querySelectorAll(".number");

form1.addEventListener("submit", function (e) {
    e.preventDefault();
    const formData = new FormData(form1);

    fetch("/classify", {
        method: "POST",
        body: formData
    })
    .then(res => {
        if (!res.ok) throw new Error("Server error");
        return res.json();
    })
    .then(data => {
        const probs = data.probabilities;
        const targets = [probs[3], probs[0], probs[1], probs[2]]; // Virus, Bacteria, Human, Plant order

        circles.forEach((circle, index) => {
            const num = numbers[index];
            const radius = circle.r.baseVal.value;
            const circumference = 2 * Math.PI * radius;

            circle.style.strokeDasharray = `${circumference}`;
            circle.style.strokeDashoffset = circumference;

            let counter = 0;
            num.innerText = "0%";

            const interval = setInterval(() => {
                if (counter >= targets[index]) {
                    clearInterval(interval);
                    num.innerText = targets[index] + "%";
                } else {
                    counter++;
                    num.innerText = counter + "%";
                    const offset = circumference - (circumference * counter) / 100;
                    circle.style.strokeDashoffset = offset;
                }
            }, 20);
        });

        // Fill results
        document.getElementById("sequence_val").innerText = truncateDNAEnd(data.sequence, 30);
        document.getElementById("num_nucleotides_val").innerText = data.num_nucleotides;
        document.getElementById("predicted_class_val").innerText = data.predicted_class;
        document.getElementById("confidence_val").innerText = data.confidence.toFixed(1) + "%";
        document.getElementById("motifs_val").innerText = data.detected_motifs.join(", ");
        document.getElementById("accuracy_val").innerText = data.model_accuracy;
        document.getElementById("interpretation_val").innerText = data.interpretation;
    })
    .catch(err => {
        console.error(err);
        alert("Please Enter a valid DNA Sequence");
    });
});

// ==== 2. DROPDOWN SELECTION (CRITICAL FIX) ====
document.querySelectorAll(".dropdown-item").forEach(item => {
    item.addEventListener("click", function () {
        const text = this.textContent;
        document.querySelector(".dropdown-toggle").textContent = text;
        document.getElementById("class_label_input").value = text;  // ← This line was missing!
    });
});

// ==== 3. ADD TO DATASET ====
document.getElementById("add_to_dataset").addEventListener("click", () => {
    const seq = document.querySelector('input[name="new_sequence"]').value.trim();
    const cls = document.getElementById("class_label_input").value;

    if (!seq || !cls || cls === "Select Class") {
        alert("Please enter a DNA sequence and select a class!");
        return;
    }

    const formData = new FormData(document.getElementById("data_input"));

    fetch("/add_to_dataset", {
        method: "POST",
        body: formData
    })
    .then(res => {
        if (!res.ok) {
            return res.text().then(text => { throw new Error(text); });
        }
        return res.json();
    })
    .then(data => {
        alert(data.message || "Added successfully!");
        document.getElementById("data_input").reset();
        document.querySelector(".dropdown-toggle").textContent = "Select Class";
    })
    .catch(err => {
        console.error("Add to dataset error:", err);
        alert("Failed to add data: " + err.message);
    });
});

// ==== 4. RETRAIN MODEL ====
document.getElementById("retrain_model").addEventListener("click", () => {
    if (!confirm("Retraining takes 30–90 seconds. Continue?")) return;

    const btn = document.getElementById("retrain_model");
    const btn1 = document.getElementById("add_to_dataset");
    const btn2 = document.getElementById("reset_dataset");
    const btn3 = document.getElementById("classify");
    btn.disabled = true;
    btn1.disabled = true;
    btn2.disabled = true;
    btn3.disabled = true;
    btn.innerText = "Retraining...";

    fetch("/retrain_model", { method: "POST" })
    .then(res => {
        if (!res.ok) throw new Error("Server error " + res.status);
        return res.json();
    })
    .then(data => {
        alert(data.message);
        location.reload(); // Reload page to use new model
    })
    .catch(err => {
        alert("Retraining failed: " + err.message);
    })
    .finally(() => {
        btn.disabled = false;
        btn1.disabled = false;
        btn2.disabled = false;
        btn3.disabled = false;
        btn.innerText = "Retrain Model";
    });
});

// ==== 5. RESET DATASET ====
document.getElementById("reset_dataset").addEventListener("click", () => {
    if (!confirm("This will DELETE all added sequences and restore original dataset. Sure?")) return;

    fetch("/reset_dataset", { method: "POST" })  // ← Make sure this matches your Flask route!
    .then(res => {
        if (!res.ok) throw new Error("Server error");
        return res.json();
    })
    .then(data => {
        alert(data.message);
        location.reload();
    })
    .catch(err => {
        alert("Reset failed: " + err.message);
    });
});

// Helper
function truncateDNAEnd(dna, max = 30) {
    return dna.length <= max ? dna : dna.slice(0, max) + "...";

}
