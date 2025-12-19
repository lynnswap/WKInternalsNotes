# ``WKInternalsNotes/WKProcessPool/_setUsesOnlyHIDGamepadProviderForTesting(_:)``

HID のみのゲームパッドプロバイダを使用する設定にする（テスト用）。

## Objective-C Declaration
```objective-c
- (void)_setUsesOnlyHIDGamepadProviderForTesting:(BOOL)usesHIDProvider WK_API_AVAILABLE(macos(11.0), ios(14.0));
```

## Discussion
`setUsesOnlyHIDGamepadProviderForTesting(usesHIDProvider)` を呼び出す。

## References
- [`WKProcessPoolPrivate.h#L192`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPoolPrivate.h#L192)
- [`WKProcessPool.mm#L670`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPool.mm#L670)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
