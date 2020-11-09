import React from "react";

const Main = () => {
  const [file, setFile] = React.useState("");

  const handleUpload = (event) => {
    setFile(event.target.files[0]);
  };

  const handleClassify = () => {
    if (file) {
      let formData = new FormData();
      formData.append("uploaded_image", file);

      fetch("api", {
        method: "POST",
        body: formData,
      })
        .then((response) => response.json())
        .then((data) => console.log(data));
    }
  };

  return (
    <div>
      <input type="file" onChange={handleUpload} />
      <button onClick={handleClassify}>Upload</button>
    </div>
  );
};

export default Main;
