const ucList = [
  { name: "30 UC", price: 7000 },
  { name: "60 UC", price: 12000 },
  { name: "120 UC", price: 24000 },
  { name: "180 UC", price: 36000 },
  { name: "325 UC", price: 57000 },
  { name: "385 UC", price: 69000 },
  { name: "415 UC", price: 73000 },
  { name: "535 UC", price: 96000 },
  { name: "660 UC", price: 115000 },
  { name: "840 UC", price: 148000 },
  { name: "900 UC", price: 160000 },
  { name: "985 UC", price: 171000 },
  { name: "1195 UC", price: 217000 },
  { name: "1320 UC", price: 227000 },
  { name: "1500 UC", price: 261000 },
  { name: "1800 UC", price: 281000 },
  { name: "2125 UC", price: 341000 },
  { name: "2460 UC", price: 341000 },
  { name: "2785 UC", price: 447000 },
  { name: "3150 UC", price: 511000 },
  { name: "3850 UC", price: 551000 },
  { name: "5650 UC", price: 831000 },
  { name: "6310 UC", price: 947000 },
  { name: "8100 UC", price: 1090000 },
  { name: "11950 UC", price: 1640000 },
  { name: "16200 UC", price: 2180000 }
];

let cart = [];

function showSection(id) {
  document.querySelectorAll(".section").forEach(sec => sec.style.display = "none");
  document.getElementById(id).style.display = "block";
}

function renderUCGrid() {
  const ucGrid = document.getElementById("ucGrid");
  ucGrid.innerHTML = "";
  ucList.forEach(item => {
    const card = document.createElement("div");
    card.className = "uc-card";
    card.textContent = item.name;

    card.title = `${item.price.toLocaleString()} UZS`;

    card.onclick = () => {
      addToCart(item);
      showToast(`${item.name} savatga tushdi!`);
    };

    ucGrid.appendChild(card);
  });
}

function addToCart(item) {
  cart.push(item);
  renderCart();
}

function renderCart() {
  const cartItems = document.getElementById("cartItems");
  const totalPrice = document.getElementById("totalPrice");
  cartItems.innerHTML = cart.map(i => `<p>${i.name} - ${i.price.toLocaleString()} UZS</p>`).join('');
  const total = cart.reduce((sum, i) => sum + i.price, 0);
  totalPrice.textContent = `Jami: ${total.toLocaleString()} UZS`;
}

function showToast(message) {
  const toast = document.getElementById("toast");
  toast.textContent = message;
  toast.className = "toast show";
  setTimeout(() => {
    toast.className = "toast";
  }, 2500);
}

window.onload = () => {
  renderUCGrid();
};
