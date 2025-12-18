# ``WKInternalsNotes/WKView/_topContentInset``

トップコンテンツ inset を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setTopContentInset:) CGFloat _topContentInset;
```

## Default Value
`0`。

## Discussion
getter は `0` を返し、setter は空実装。

## References
- [`WKViewPrivate.h#L70`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKViewPrivate.h#L70)
- [`WKView.mm#L1223`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/mac/WKView.mm#L1223)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
