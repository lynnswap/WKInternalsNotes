# ``WKInternalsNotes/WKMouseDeviceObserver/start()``

マウスデバイスの接続監視を開始する。

## Objective-C Declaration
```objective-c
- (void)start;
```

## Discussion
`startCount` をインクリメントし、初回のみ `NotificationCenter` の接続/切断通知を監視する Task を開始する。

## References
- [WKMouseDeviceObserver.h#L38](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKMouseDeviceObserver.h#L38)
- [WKMouseDeviceObserver.swift#L67](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/WKMouseDeviceObserver.swift#L67)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
