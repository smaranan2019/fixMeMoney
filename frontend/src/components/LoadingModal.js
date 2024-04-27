import React from 'react';
import Modal from 'react-modal';

function LoadingModal(props) {
  const customStyles = {
    content: {
      top: '50%',
      left: '50%',
      right: 'auto',
      bottom: 'auto',
      marginRight: '-50%',
      transform: 'translate(-50%, -50%)',
      borderRadius: '15px'
    },
  };

  const spinnerStyles = {
    width: "3rem",
    height: "3rem",
    marginLeft: "15px",
    marginRight: "15px"
  }

  return (
    <div>
      <Modal
        style={customStyles}
        isOpen={props.shouldOpen}
        contentLabel="Example Modal"
      >
        <div class="spinner-border" style={spinnerStyles} role="status">
          <span class="sr-only">Loading...</span>
        </div>
      </Modal>
    </div>
  );
}

export default LoadingModal;
