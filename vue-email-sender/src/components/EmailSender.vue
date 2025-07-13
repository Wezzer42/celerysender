<template>
  <div class="min-h-screen flex items-center justify-center bg-gray-900 p-4">
    <div class="bg-gray-800 p-8 rounded-lg shadow-lg w-full max-w-md">
      <h2 class="text-2xl font-semibold text-white mb-6 text-center">Send Email</h2>
      <form @submit.prevent="submit" class="space-y-4">
        <div>
          <label class="block text-sm text-gray-300">Email</label>
          <input
            v-model="form.email"
            type="email"
            placeholder="you@example.com"
            class="mt-1 w-full px-3 py-2 bg-gray-700 border border-gray-600 rounded focus:outline-none focus:ring-2 focus:ring-blue-500 text-white"
          />
          <p v-if="errors.email" class="text-red-400 text-xs mt-1">{{ errors.email }}</p>
        </div>
        <div>
          <label class="block text-sm text-gray-300">Subject</label>
          <input
            v-model="form.subject"
            placeholder="Subject"
            class="mt-1 w-full px-3 py-2 bg-gray-700 border border-gray-600 rounded focus:outline-none focus:ring-2 focus:ring-blue-500 text-white"
          />
          <p v-if="errors.subject" class="text-red-400 text-xs mt-1">{{ errors.subject }}</p>
        </div>
        <div>
          <label class="block text-sm text-gray-300">Message</label>
          <textarea
            v-model="form.message"
            rows="4"
            placeholder="Your message..."
            class="mt-1 w-full px-3 py-2 bg-gray-700 border border-gray-600 rounded focus:outline-none focus:ring-2 focus:ring-blue-500 text-white"
          ></textarea>
          <p v-if="errors.message" class="text-red-400 text-xs mt-1">{{ errors.message }}</p>
        </div>
        <button
          :disabled="loading"
          class="w-full flex items-center justify-center bg-blue-600 hover:bg-blue-700 disabled:bg-gray-600 text-white font-semibold py-2 rounded transition duration-200"
        >
          <svg
            v-if="loading"
            class="animate-spin h-5 w-5 mr-2 text-white"
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
          >
            <circle
              class="opacity-25"
              cx="12"
              cy="12"
              r="10"
              stroke="currentColor"
              stroke-width="4"
            ></circle>
            <path
              class="opacity-75"
              fill="currentColor"
              d="M4 12a8 8 0 018-8v8z"
            ></path>
          </svg>
          <span v-if="!loading">Send</span>
          <span v-else>Sending...</span>
        </button>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { useToast } from "vue-toastification";

const toast = useToast();
const form = ref({
  email: "",
  subject: "",
  message: "",
});

const loading = ref(false);
const success = ref(false);
const error = ref("");
const errors = ref({
  email: "",
  subject: "",
  message: "",
});

function validate() {
  errors.value = { email: "", subject: "", message: "" };
  let valid = true;

  if (!form.value.email) {
    errors.value.email = "Email is required.";
    valid = false;
  } else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(form.value.email)) {
    errors.value.email = "Enter a valid email.";
    valid = false;
  }

  if (!form.value.subject) {
    errors.value.subject = "Subject is required.";
    valid = false;
  }

  if (!form.value.message) {
    errors.value.message = "Message is required.";
    valid = false;
  }

  return valid;
}

async function submit() {
  if (!validate()) return;

  loading.value = true;

  try {
    const response = await fetch("http://localhost:8000/api/send-email/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(form.value),
    });
    if (response.ok) {
      toast.success("Email успешно поставлен в очередь!");
      form.value = { email: "", subject: "", message: "" };
    } else {
      const data = await response.json();
      toast.error("Ошибка: " + JSON.stringify(data));
    }
  } catch (e) {
    toast.error("Ошибка: " + e.message);
  } finally {
    loading.value = false;
  }
}
</script>
