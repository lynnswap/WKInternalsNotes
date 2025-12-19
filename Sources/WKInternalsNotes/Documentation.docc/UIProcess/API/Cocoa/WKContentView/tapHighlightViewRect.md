# ``WKInternalsNotes/WKContentView/tapHighlightViewRect``

タップハイライト表示ビューのフレーム矩形を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) CGRect tapHighlightViewRect;
```

## Default Value
`_tapHighlightView` の `frame` を返す。

## Discussion
`_tapHighlightView` の `frame` を返す単純な getter。

## References
- [`WKContentViewInteraction.h#L737`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L737)
- [`WKContentViewInteraction.mm#L2610`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L2610)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
