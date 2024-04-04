import * as React from "react";
import SpeakerNotesIcon from "@mui/icons-material/SpeakerNotes";
import {
  Button,
  Divider,
  Grid,
  IconButton,
  Modal,
  Paper,
  Typography,
} from "@mui/material";
import { styled } from "@mui/material/styles";
import CloseIcon from "@mui/icons-material/Close";
import HistoryContainer from "./HistoryContainer";

const HistoryModal = styled(Paper)(({ theme }) => ({
  position: "absolute",
  top: "50%",
  left: "50%",
  transform: "translate(-50%, -50%)",
  width: "100%",
  maxHeight:'100%',
  // overflow:'auto',
  padding: theme.spacing(2),
  ...theme.typography.body2,
  textAlign: "center",
  [theme.breakpoints.up("sm")]: {
    width: "400px",
    maxHeight:'500px',
  },
}));

export default function History() {
  const [open, setOpen] = React.useState(false);
  const handleOpen = () => setOpen(true);
  const handleClose = () => setOpen(false);

  return (
    <div>
      <Button
        type="button"
        variant="outlined"
        endIcon={<SpeakerNotesIcon />}
        onClick={handleOpen}
      >
        History
      </Button>
      <Modal
        open={open}
        onClose={handleClose}
        aria-labelledby="history-modal"
        aria-describedby="history-modal"
      >
        <HistoryModal>
          <Grid container justifyContent={"flex-start"}>
            <Grid item flexGrow={1}>
              <Typography variant="h6" component="h2">
                Exchange history
              </Typography>
            </Grid>
            <Grid item>
              <IconButton
                color="primary"
                aria-label="upload picture"
                component="span"
                onClick={handleClose}
              >
                <CloseIcon />
              </IconButton>
            </Grid>
          </Grid>

          <Divider />
          <HistoryContainer />
        </HistoryModal>
      </Modal>
    </div>
  );
}
