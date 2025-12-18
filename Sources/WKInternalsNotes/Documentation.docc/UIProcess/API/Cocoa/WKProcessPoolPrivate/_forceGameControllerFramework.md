# ``WKInternalsNotes/WKProcessPool/_forceGameControllerFramework()``

GameController.framework を使うゲームパッドプロバイダに固定する。

## Objective-C Declaration
```objective-c
+ (void)_forceGameControllerFramework WK_API_AVAILABLE(macos(10.13), ios(11.0));
```

## Discussion
`ENABLE(GAMEPAD)` の場合に `UIGamepadProvider::setUsesGameControllerFramework()` を呼び出す。

## References
- [`WKProcessPoolPrivate.h#L161`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPoolPrivate.h#L161)
- [`WKProcessPool.mm#L530`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPool.mm#L530)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
