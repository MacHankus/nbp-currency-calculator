import * as React from 'react'
import InputLabel from '@mui/material/InputLabel'
import FormControl from '@mui/material/FormControl'
import { TextField, TextFieldProps } from '@mui/material'

interface IValueInputProps {
  onChangeHandle: (event: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => void
}

export default function ValueInput({ onChangeHandle, ...props }: IValueInputProps & Omit<TextFieldProps, 'variant'>) {
  return (
    <FormControl fullWidth variant="outlined">
      <InputLabel htmlFor="outlined-adornment-password">{props.children}</InputLabel>
      <TextField
        id="id-value-input"
        type="number"
        label="Value"
        onChange={onChangeHandle}
        {...props}
      />
    </FormControl>
  )
}
