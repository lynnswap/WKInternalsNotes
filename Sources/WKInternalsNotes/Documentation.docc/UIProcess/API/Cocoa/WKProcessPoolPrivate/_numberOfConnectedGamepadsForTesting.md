# ``WKInternalsNotes/WKProcessPool/_numberOfConnectedGamepadsForTesting()``

接続されているゲームパッド数を返す（テスト用）。

## Objective-C Declaration
```objective-c
- (size_t)_numberOfConnectedGamepadsForTesting WK_API_AVAILABLE(macos(11.0), ios(14.0));
```

## Discussion
`numberOfConnectedGamepadsForTesting(GamepadType::All)` を返す。

## References
- [`WKProcessPoolPrivate.h#L189`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPoolPrivate.h#L189)
- [`WKProcessPool.mm#L655`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPool.mm#L655)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
