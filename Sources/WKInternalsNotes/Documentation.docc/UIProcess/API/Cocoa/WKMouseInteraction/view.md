# ``WKInternalsNotes/WKMouseInteraction/view``

関連付けられたビューを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, weak, readonly) UIView *view;
```

## Default Value
`didMoveToView:` で設定される。

## Discussion
`_view` をそのまま返す。

## References
- [`WKMouseInteraction.h#L46`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKMouseInteraction.h#L46)
- [`WKMouseInteraction.mm#L195`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKMouseInteraction.mm#L195)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
