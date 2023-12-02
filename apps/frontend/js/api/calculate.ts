import urls from './urls'
import axios, { AxiosResponse } from "axios";
import CalculateDTO from '../interfaces/calculate-dto'
import { ApiError } from './exceptions';

interface postCalculateResponse {
  value: number
}

export async function postCalculate(toCalculate: CalculateDTO): Promise<void>{
  try {
      const response = await axios.post<postCalculateResponse>(urls.CALCULATE, toCalculate)
  }catch(err){
    console.log(err)
    throw new ApiError("Api Error", "")
  }
  
}