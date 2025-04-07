function openModal(studentName, documentType, status, dateRequested) {
  document.getElementById('uniqueRequestDetails').innerHTML = `
      <p><strong>Student Name:</strong> ${studentName}</p>
      <p><strong>Document Type:</strong> ${documentType}</p>
      <p><strong>Status:</strong> ${status}</p>
      <p><strong>Date Requested:</strong> ${dateRequested}</p>
  `;

  const overlay = Object.assign(document.createElement('div'), {
      id: 'modal-overlay',
      style: 'position:fixed;top:0;left:0;width:100%;height:100%;background:rgba(0,0,0,0.5);z-index:999;pointer-events:auto;'
  });

  document.body.appendChild(overlay);

  Object.assign(document.getElementById('uniqueViewRequestModal').style, {
      display: 'flex', opacity: '1', visibility: 'visible', zIndex: '1000'
  });
}

function closeModal() {
  document.getElementById('uniqueViewRequestModal').style = 'display:none;opacity:0;visibility:hidden';
  document.getElementById('modal-overlay')?.remove();
}
