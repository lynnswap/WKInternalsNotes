# ``WKInternalsNotes/WKMouseDeviceObserver/sharedInstance()``

共有インスタンスを返す。

## Objective-C Declaration
```objective-c
+ (WKMouseDeviceObserver *)sharedInstance;
```

## Discussion
Swift 実装では `private static let shared` を返すシングルトン。

## References
- [WKMouseDeviceObserver.h#L35](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKMouseDeviceObserver.h#L35)
- [WKMouseDeviceObserver.swift#L63](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/WKMouseDeviceObserver.swift#L63)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
