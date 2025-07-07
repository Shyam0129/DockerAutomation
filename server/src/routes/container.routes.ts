import { Router } from "express";
import {
  containerCreate,
  containerListAll,
  containerStart,
  containerStop,
  restartContainer,
} from "../controller/container.controller";

export const router = Router();

router.get("/all", containerListAll);
router.post("/create", containerCreate);
router.post("/start", containerStart);
router.post("/stop", containerStop);
router.post('/restart', restartContainer);