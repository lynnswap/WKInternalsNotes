# ``WKInternalsNotes/WKMouseInteraction/mouseTouchGestureRecognizer``

マウスクリック用のジェスチャレコグナイザを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) UIGestureRecognizer *mouseTouchGestureRecognizer;
```

## Default Value
`initWithDelegate:` で生成した `WKMouseTouchGestureRecognizer`。

## Discussion
`_mouseTouchGestureRecognizer` を返す。

## References
- [`WKMouseInteraction.h#L59`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKMouseInteraction.h#L59)
- [`WKMouseInteraction.mm#L232`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKMouseInteraction.mm#L232)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
