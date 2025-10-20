import { useState, useEffect } from "react";

const ContactForm = ({ existingContact = {}, updateCallback }) => {
  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState("");
  const [email, setEmail] = useState("");

  useEffect(() => {
    setFirstName(existingContact.firstName || "");
    setLastName(existingContact.lastName || "");
    setEmail(existingContact.email || "");
  }, [existingContact]);

  const updating = existingContact && existingContact.id !== undefined;

  const onSubmit = async (e) => {
    e.preventDefault();

    const data = {
      firstName: firstName.trim(),
      lastName: lastName.trim(),
      email: email.trim()
    };

    if (!data.firstName || !data.lastName || !data.email) {
      alert("Compila tutti i campi correttamente");
      return;
    }

    const url = updating
      ? `http://127.0.0.1:5000/update_contact/${existingContact.id}`
      : "http://127.0.0.1:5000/create_contact";

    const options = {
      method: updating ? "PATCH" : "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(data)
    };

    const response = await fetch(url, options);
    if (response.status === 200 || response.status === 201) {
      updateCallback();
    } else {
      const resData = await response.json();
      alert(resData.message);
    }
  };

  return (
    <form onSubmit={onSubmit}>
      <div>
        <label htmlFor="firstName">First Name:</label>
        <input
          type="text"
          id="firstName"
          value={firstName}
          onChange={(e) => setFirstName(e.target.value)}
          placeholder="First Name"
          required
        />
      </div>
      <div>
        <label htmlFor="lastName">Last Name:</label>
        <input
          type="text"
          id="lastName"
          value={lastName}
          onChange={(e) => setLastName(e.target.value)}
          placeholder="Last Name"
          required
        />
      </div>
      <div>
        <label htmlFor="email">Email:</label>
        <input
          type="text"
          id="email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          placeholder="Email"
          required
        />
      </div>
      <button type="submit">{updating ? "Update" : "Create"}</button>
    </form>
  );
};

export default ContactForm;
