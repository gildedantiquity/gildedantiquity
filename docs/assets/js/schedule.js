(() => {
  const root = document.querySelector("[data-schedule]");
  if (!root) return;

  const formatDate = (iso) => {
    const d = new Date(`${iso}T00:00:00`);
    return new Intl.DateTimeFormat("id-ID", {
      weekday: "short",
      day: "numeric",
      month: "short",
      year: "numeric",
    }).format(d);
  };

  const render = (data) => {
    const cadence = document.querySelector("[data-cadence]");
    if (cadence) cadence.textContent = data.cadence;

    const rows = data.posts
      .map((post) => {
        const statusClass = post.status === "live" ? "status-live" : "status-planned";
        const statusLabel = post.status === "live" ? "Tayang" : "Terjadwal";
        const titleCell =
          post.status === "live"
            ? `<a href="posts/${post.slug}.html">${post.title}</a>`
            : post.title;

        return `
          <tr class="reveal">
            <td class="day">${formatDate(post.date)}</td>
            <td>
              <strong>${titleCell}</strong>
              <div class="tag">${post.theme}</div>
              <p style="margin:0.4rem 0 0;color:var(--muted);font-size:0.95rem">${post.summary}</p>
            </td>
            <td class="status ${statusClass}">${statusLabel}</td>
          </tr>
        `;
      })
      .join("");

    root.innerHTML = `
      <table class="schedule-table">
        <thead>
          <tr>
            <th>Tanggal</th>
            <th>Topik</th>
            <th>Status</th>
          </tr>
        </thead>
        <tbody>${rows}</tbody>
      </table>
    `;

    document.querySelectorAll(".reveal").forEach((el) => {
      el.classList.add("is-visible");
    });
  };

  fetch("assets/data/schedule.json")
    .then((res) => {
      if (!res.ok) throw new Error("Gagal memuat jadwal");
      return res.json();
    })
    .then(render)
    .catch(() => {
      root.innerHTML = `<p>Jadwal belum bisa dimuat. Coba refresh halaman.</p>`;
    });
})();
