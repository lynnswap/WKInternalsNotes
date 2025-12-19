# ``WKInternalsNotes/WKMouseDeviceObserver/hasMouseDevice``

マウスポインティングデバイスが接続されているかを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) BOOL hasMouseDevice;
```

## Default Value
`connectedDeviceCount > 0` の結果を返す。

## Discussion
Swift 実装では `connectedDeviceCount` を監視し、0 より大きい場合に `true` を返す。`start()` で通知監視を開始し、接続/切断でカウントを更新する。

## References
- [WKMouseDeviceObserver.h#L41](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKMouseDeviceObserver.h#L41)
- [WKMouseDeviceObserver.swift#L56](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/WKMouseDeviceObserver.swift#L56)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
