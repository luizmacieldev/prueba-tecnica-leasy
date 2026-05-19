import { FormEvent, useState } from "react"

import {
  cancelReservation,
  getReservations,
  login,
} from "./services/api"

import type {
  Reservation,
} from "./types/api"

function App() {
  const [email, setEmail] = useState("")
  const [password, setPassword] = useState("")
  const [token, setToken] = useState("")

  const [reservations, setReservations] =
    useState<Reservation[]>([])

  const [error, setError] = useState("")
  const [loading, setLoading] = useState(false)

  const [cancelReason, setCancelReason] =
    useState("")

  const [selectedReservationId, setSelectedReservationId] =
    useState<string | null>(null)

  async function handleLogin(
    event: FormEvent,
  ) {
    event.preventDefault()

    try {
      setLoading(true)
      setError("")

      const response = await login(
        email,
        password,
      )

      setToken(response.access_token)

      const reservationsData =
        await getReservations(
          response.access_token,
        )

      setReservations(reservationsData)

    } catch (err) {
      setError(
        err instanceof Error
          ? err.message
          : "Unexpected error",
      )

    } finally {
      setLoading(false)
    }
  }

  async function handleCancelReservation(
    reservationId: string,
  ) {
    try {
      setError("")

      const updatedReservation =
        await cancelReservation(
          token,
          reservationId,
          cancelReason,
        )

      setReservations((current) =>
        current.map((reservation) =>
          reservation.id === reservationId
            ? updatedReservation
            : reservation
        )
      )

      setSelectedReservationId(null)
      setCancelReason("")

    } catch (err) {
      setError(
        err instanceof Error
          ? err.message
          : "Unexpected error",
      )
    }
  }

  return (
    <div className="min-h-screen bg-gray-100 p-8">
      <div className="max-w-3xl mx-auto bg-white p-8 rounded-xl shadow">

        <h1 className="text-3xl font-bold mb-8">
          Client Portal
        </h1>

        {error && (
          <div className="bg-red-100 text-red-700 p-3 rounded-lg mb-6">
            {error}
          </div>
        )}

        {!token && (
          <form
            onSubmit={handleLogin}
            className="flex flex-col gap-4"
          >
            <input
              type="email"
              placeholder="Email"
              value={email}
              onChange={(event) =>
                setEmail(event.target.value)
              }
              className="border rounded-lg p-3"
            />

            <input
              type="password"
              placeholder="Password"
              value={password}
              onChange={(event) =>
                setPassword(event.target.value)
              }
              className="border rounded-lg p-3"
            />

            <button
              type="submit"
              disabled={loading}
              className="bg-black text-white rounded-lg p-3"
            >
              {loading
                ? "Loading..."
                : "Login"}
            </button>
          </form>
        )}

        {token && (
          <div>
            <h2 className="text-2xl font-semibold mb-6">
              My Reservations
            </h2>

            <div className="space-y-4">
              {reservations.map(
                (reservation) => (
                  <div
                    key={reservation.id}
                    className="border rounded-xl p-5"
                  >
                    <p>
                      <strong>Room:</strong>{" "}
                      {reservation.room_name}
                    </p>

                    <p>
                      <strong>Status:</strong>{" "}
                      {reservation.status}
                    </p>

                    <p>
                      <strong>Starts:</strong>{" "}
                      {new Date(
                      reservation.starts_at,
                    ).toLocaleString()}
                    </p>

                    <p>
                      <strong>Ends:</strong>{" "}
                      {new Date(
                        reservation.ends_at,
                      ).toLocaleString()}
                    </p>

                    {reservation.cancel_reason && (
                      <p>
                        <strong>
                          Cancel reason:
                        </strong>{" "}
                        {
                          reservation.cancel_reason
                        }
                      </p>
                    )}

                    {["requested", "confirmed"].includes(
                      reservation.status,
                    ) && (
                      <div className="mt-4">
                        {selectedReservationId ===
                        reservation.id ? (
                          <div className="flex flex-col gap-3">
                            <textarea
                              placeholder="Cancellation reason"
                              value={cancelReason}
                              onChange={(event) =>
                                setCancelReason(
                                  event.target.value,
                                )
                              }
                              className="border rounded-lg p-3"
                            />

                            <div className="flex gap-2">
                              <button
                                onClick={() =>
                                  handleCancelReservation(
                                    reservation.id,
                                  )
                                }
                                className="bg-red-600 text-white px-4 py-2 rounded-lg"
                              >
                                Confirm cancellation
                              </button>

                              <button
                                onClick={() => {
                                  setSelectedReservationId(
                                    null,
                                  )

                                  setCancelReason("")
                                }}
                                className="border px-4 py-2 rounded-lg"
                              >
                                Cancel
                              </button>
                            </div>
                          </div>
                        ) : (
                          <button
                            onClick={() =>
                              setSelectedReservationId(
                                reservation.id,
                              )
                            }
                            className="bg-black text-white px-4 py-2 rounded-lg mt-3"
                          >
                            Cancel reservation
                          </button>
                        )}
                      </div>
                    )}
                  </div>
                ),
              )}
            </div>
          </div>
        )}
      </div>
    </div>
  )
}

export default App