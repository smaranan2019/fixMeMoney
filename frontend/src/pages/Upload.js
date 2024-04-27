import React, { Component } from 'react';
import axios from 'axios';
import CONFIG from '../config';
import LoadingModel from "../components/LoadingModal";


class Upload extends Component {
  constructor(props) {
    super(props);

    this.state = {
      bank_statement: null,
      error: null,
      loading: false
    }
    this.handleSubmit = this.handleSubmit.bind(this);
    this.handleFileUpload = this.handleFileUpload.bind(this);
  }

  handleFileUpload(e) {
    const file = e.target.files[0];
    this.setState({
      bank_statement: file,
      error: null
    })
  }

  handleSubmit(e) {
    e.preventDefault();
    if (!this.state.bank_statement) return

    const formData = new FormData();
    formData.append("file", this.state.bank_statement);
    this.setState({loading: true})
    axios.post(CONFIG.ocr_api, formData, {
      headers: {
        "Content-Type": "multipart/form-data",
      }
    })
      .then((response) => {
        console.log("successfully uploaded")
        //TO-DO: redirect to transaction page?
      }).catch((error) => {
        // handle errors
        this.setState({ error: error.response.data });
        console.log(error);
      }).finally(() => {
        this.setState({loading: false})
      });
  }

  render() {
    return (
      <>
        <LoadingModel shouldOpen={this.state.loading}/>
        <div className="main-container">
          <section className="height-100 bg-dark">
            <div className="container">
              <div className="row">
                {this.state.error && <div class="alert alert-danger" role="alert">
                  {this.state.error}
                </div>}
              </div>
              <div className="row">
                <form onSubmit={this.handleSubmit}>
                  <div class="mb-3">
                    <label for="formFile" class="form-label">Upload Bank Statement (PDF)</label>
                    <input class="form-control" type="file" id="formFile" onChange={this.handleFileUpload} />
                  </div>
                  <button type="submit" class="btn btn-primary">Upload</button>
                </form>
              </div>
            </div>
          </section>
        </div>
      </>
    );
  }
}

export default Upload;
