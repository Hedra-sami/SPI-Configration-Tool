/***********************************************************
 * MSPI_Config.h
 *
 * Created on: 11/04/2023
 * Author: hedra
 * SWC:   SPI                                              
 * Layer: MCAL                                             
 **********************************************************/ 


#ifndef MSPI_CONFIG_H_
#define MSPI_CONFIG_H_

#define MSPI1_STATUS         MSPI_DISABLE

#define MSPI1_CLOCK_MODE     MSPI_MODE1

#define MSPI1_MASTER_SLAVE   MSPI_MASTER

#define MSPI1_PRESCALLER     MSPI_FPCLK_DIVIDED_BY_8

#define MSPI1_DATA_ORDER     MSPI_LSB_FIRST

#define MSPI1_SS_MANAGE      MSPI_HW_SLAVE_MANAGEMENT

#define MSPI1_DATA_SIZE      MSPI_16BIT_DATA

#define MSPI1_TX_INT_STATUS  MSPI_INT_ENABLE

#define MSPI1_RX_INT_STATUS  MSPI_INT_ENABLE

#define MSPI_SS_PORT         PORTA

#define MSPI_SS_PIN          PIN0


#endif
