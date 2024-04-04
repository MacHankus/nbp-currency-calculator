import urls from './urls'
import axios from "axios";
import CalculateDTO from '../interfaces/calculate-dto'
import { ApiError, ApiWrongResponse } from './exceptions';
import IPostCalculateResponse from './interfaces/post-calculate-response';



export async function postCalculate(toCalculate: CalculateDTO): Promise<IPostCalculateResponse>{
  try {
      const response = await axios.post<IPostCalculateResponse>(urls.CALCULATE, toCalculate)
      if (response.status != 200){
        throw new ApiWrongResponse("Wrong response", "Status code: " + response.status.toString())
      }
      return response.data
  }catch(err){
    console.log(err)
    throw new ApiError("Api Error", "")
  }
  
}