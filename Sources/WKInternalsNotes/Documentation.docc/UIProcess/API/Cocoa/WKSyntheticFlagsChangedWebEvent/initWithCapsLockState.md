# ``WKInternalsNotes/WKSyntheticFlagsChangedWebEvent/initWithCapsLockState(_:)``

Caps Lock の状態変化イベントを生成する。

## Objective-C Declaration
```objective-c
- (instancetype)initWithCapsLockState:(BOOL)keyDown;
```

## Discussion
`kHIDUsage_KeyboardCapsLock` と `WebEventFlagMaskLeftCapsLockKey` を使って `initWithKeyCode:modifiers:keyDown:` を呼ぶ。

## References
- [`WKSyntheticFlagsChangedWebEvent.h#L32`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKSyntheticFlagsChangedWebEvent.h#L32)
- [`WKSyntheticFlagsChangedWebEvent.mm#L39`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKSyntheticFlagsChangedWebEvent.mm#L39)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
