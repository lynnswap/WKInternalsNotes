# ``WKInternalsNotes/WKMouseDeviceObserver/stop()``

マウスデバイスの接続監視を停止する。

## Objective-C Declaration
```objective-c
- (void)stop;
```

## Discussion
`startCount` をデクリメントし、0 になった時点で接続/切断監視 Task をキャンセルする。

## References
- [WKMouseDeviceObserver.h#L39](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKMouseDeviceObserver.h#L39)
- [WKMouseDeviceObserver.swift#L94](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/WKMouseDeviceObserver.swift#L94)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
