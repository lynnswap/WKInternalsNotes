# ``WKInternalsNotes/WKMouseDeviceObserver/_setHasMouseDevice(forTesting:)``

テスト用に接続状態を強制設定する。

## Swift Declaration
```swift
func _setHasMouseDevice(forTesting hasMouseDevice: Bool)
```

## Discussion
Swift 実装では `connectedDeviceCount` を 1/0 に切り替え、接続状態を疑似的に変更する。

## References
- [WKMouseDeviceObserver.swift#L110](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/WKMouseDeviceObserver.swift#L110)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
