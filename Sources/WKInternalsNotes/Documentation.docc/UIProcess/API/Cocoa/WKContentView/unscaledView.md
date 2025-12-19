# ``WKInternalsNotes/WKContentView/unscaledView``

スケール前のインタラクション用ビューを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) UIView *unscaledView;
```

## Default Value
`_interactionViewsContainerView` を返す。

## Discussion
`_interactionViewsContainerView` を返す単純な getter。

## References
- [`WKContentViewInteraction.h#L740`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L740)
- [`WKContentViewInteraction.mm#L1815`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L1815)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
