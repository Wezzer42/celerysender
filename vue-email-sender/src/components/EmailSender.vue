<template>
  <div class="max-w-md mx-auto p-4">
    <h2 class="text-xl font-bold mb-4">Send Email</h2>
    <form @submit.prevent="submit">
      <div class="mb-2">
        <label>Email</label>
        <input v-model="form.email" type="email" class="border p-1 w-full" />
      </div>
      <div class="mb-2">
        <label>Subject</label>
        <input v-model="form.subject" class="border p-1 w-full" />
      </div>
      <div class="mb-2">
        <label>Message</label>
        <textarea v-model="form.message" class="border p-1 w-full"></textarea>
      </div>
      <button class="bg-blue-500 text-white px-4 py-2">Send</button>
    </form>
    <p v-if="success" class="text-green-600 mt-2">Email queued successfully!</p>
    <p v-if="error" class="text-red-600 mt-2">{{ error }}</p>
  </div>
</template>

<script setup>
import { ref } from "vue";

const form = ref({
  email: "",
  subject: "",
  message: "",
});

const success = ref(false);
const error = ref("");

async function submit() {
  success.value = false;
  error.value = "";
  try {
    const response = await fetch("http://localhost:8000/api/send-email/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(form.value),
    });
    if (response.ok) {
      success.value = true;
      form.value = { email: "", subject: "", message: "" };
    } else {
      const data = await response.json();
      error.value = JSON.stringify(data);
    }
  } catch (e) {
    error.value = e.message;
  }
}
</script>
