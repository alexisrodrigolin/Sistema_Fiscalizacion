#ifndef _SAM4SFISCALDRIVER_H_
#define _SAM4SFISCALDRIVER_H_

#ifdef __cplusplus
extern "C" {
#endif

int WINAPI SerialPortOpen (int comnum);
int WINAPI SerialBaudSet (int nbaud);
int WINAPI SerialPortClose ();
int WINAPI IFOpBegin (const char * name);
int WINAPI IFOpSend (int wait);
int WINAPI IFOpWaitingIs ();
int WINAPI IFOpAbort ();
int WINAPI IFOpParamSet (const char * name, const char * value);
const char * WINAPI IFOpParamGet (const char * name);
int WINAPI IFOpParamIntSet (const char * name, int value);
int WINAPI IFOpParamIntGet (const char * name);
int WINAPI IFOpParamFloatSet (const char * name, double value);
double WINAPI IFOpParamFloatGet (const char * name);
int WINAPI IFOpParamBoolSet (const char * name, int value);
int WINAPI IFOpParamBoolGet (const char * name);
int WINAPI IFOpCmdOkIs ();
int WINAPI IFOpErrorGet ();
const char * WINAPI IFOpErrorDescGet ();
int WINAPI IFOpStateGet (const char * name);
const char * WINAPI IFOpRetGet (const char * name);
int WINAPI IFOpRetIntGet (const char * name);
double WINAPI IFOpRetFloatGet (const char * name);
int WINAPI IFOpRetBoolGet (const char * name);
const char * WINAPI IFOpListGet (int idx);
const char * WINAPI IFOpParamListGet (int idx);
const char * WINAPI IFOpRetListGet (int idx);
const char * WINAPI IFOpStateListGet (int idx);

#ifdef __cplusplus
}
#endif

#endif /*_SAM4SFISCALDRIVER_H_*/
