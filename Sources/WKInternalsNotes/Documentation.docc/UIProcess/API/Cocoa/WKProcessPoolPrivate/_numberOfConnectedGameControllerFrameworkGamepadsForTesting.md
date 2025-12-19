# ``WKInternalsNotes/WKProcessPool/_numberOfConnectedGameControllerFrameworkGamepadsForTesting()``

GameController.framework 由来の接続ゲームパッド数を返す（テスト用）。

## Objective-C Declaration
```objective-c
- (size_t)_numberOfConnectedGameControllerFrameworkGamepadsForTesting WK_API_AVAILABLE(macos(11.0), ios(14.0));
```

## Discussion
`numberOfConnectedGamepadsForTesting(GamepadType::GameControllerFramework)` を返す。

## References
- [`WKProcessPoolPrivate.h#L191`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPoolPrivate.h#L191)
- [`WKProcessPool.mm#L665`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPool.mm#L665)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
