const API_BASE_URL = "http://127.0.0.1:8000/api/v1"

export async function login(
  email: string,
  password: string,
) {
  const response = await fetch(
    `${API_BASE_URL}/auth/login`,
    {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        email,
        password,
      }),
    }
  )

  const data = await response.json()

  if (!response.ok) {
    throw new Error(
      data.detail || "Error al iniciar sesión"
    )
  }

  return data
}

export async function getReservations(
  token: string,
) {
  const response = await fetch(
    `${API_BASE_URL}/reservations/`,
    {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    }
  )

  const data = await response.json()

  if (!response.ok) {
    throw new Error(
      data.detail ||
      "Error al cargar reservas"
    )
  }

  return data
}

export async function cancelReservation(
  token: string,
  reservationId: string,
  reason: string,
) {
  const response = await fetch(
    `${API_BASE_URL}/reservations/${reservationId}/cancel`,
    {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${token}`,
      },
      body: JSON.stringify({
        reason,
      }),
    }
  )

  const data = await response.json()

  if (!response.ok) {
    throw new Error(
      data.detail ||
      "Error al cancelar la reserva"
    )
  }

  return data
}