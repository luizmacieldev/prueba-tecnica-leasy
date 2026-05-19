export type LoginResponse = {
  access_token: string
  token_type: string
}

export type Reservation = {
  id: string
  room_name: string
  status: string
  starts_at: string
  ends_at: string
  cancel_reason: string | null
}

export type ProblemDetail = {
  type: string
  title: string
  status: number
  detail: string
  code: string
  instance: string
  errors: unknown[] | null
}