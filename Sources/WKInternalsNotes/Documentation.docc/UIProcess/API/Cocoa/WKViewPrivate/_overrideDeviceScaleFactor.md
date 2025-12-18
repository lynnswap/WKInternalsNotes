# ``WKInternalsNotes/WKView/_overrideDeviceScaleFactor``

デバイススケール係数の上書き値を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setOverrideDeviceScaleFactor:) CGFloat _overrideDeviceScaleFactor WK_API_AVAILABLE(macos(10.11));
```

## Default Value
`0`。

## Discussion
getter は `0` を返し、setter は空実装。

## References
- [`WKViewPrivate.h#L81`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKViewPrivate.h#L81)
- [`WKView.mm#L1187`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/mac/WKView.mm#L1187)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
