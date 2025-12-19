# ``WKInternalsNotes/WKContentView/_shouldAvoidScrollingWhenFocusedContentIsVisible``

フォーカス要素が可視のときにスクロールを避けるべきかを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) BOOL _shouldAvoidScrollingWhenFocusedContentIsVisible;
```

## Default Value
`_focusedElementInformation.shouldAvoidScrollingWhenFocusedContentIsVisible` を返す。

## Discussion
フォーカス中の要素のヒント情報に基づく単純な getter。

## References
- [`WKContentViewInteraction.h#L942`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L942)
- [`WKContentViewInteraction.mm#L10223`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L10223)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
