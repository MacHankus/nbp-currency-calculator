export class ApiGenericError extends Error {
    detail: string | null = null
    constructor(message: string, detail: string) {
      super(message)
      this.detail = detail
    }
  }

  export class ApiError extends ApiGenericError {
    constructor(message: string, detail: string) {
      super(message, detail)
      this.name = "ApiError"
    }
  }
  
  export class ApiWrongResponse extends ApiGenericError {
    constructor(message: string, detail: string) {
      super(message, detail)
      this.name = "ApiWrongResponse"
    }
  }
  
  