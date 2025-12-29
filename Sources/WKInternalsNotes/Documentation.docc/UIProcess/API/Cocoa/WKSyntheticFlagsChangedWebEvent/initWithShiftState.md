# ``WKInternalsNotes/WKSyntheticFlagsChangedWebEvent/initWithShiftState(_:)``

Shift の状態変化イベントを生成する。

## Objective-C Declaration
```objective-c
- (instancetype)initWithShiftState:(BOOL)keyDown;
```

## Discussion
`kHIDUsage_KeyboardLeftShift` と `WebEventFlagMaskLeftShiftKey` を使って `initWithKeyCode:modifiers:keyDown:` を呼ぶ。

## References
- [`WKSyntheticFlagsChangedWebEvent.h#L33`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKSyntheticFlagsChangedWebEvent.h#L33)
- [`WKSyntheticFlagsChangedWebEvent.mm#L44`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKSyntheticFlagsChangedWebEvent.mm#L44)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
