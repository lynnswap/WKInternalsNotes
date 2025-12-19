# ``WKInternalsNotes/WKContentView/_shouldAvoidResizingWhenInputViewBoundsChange``

入力ビューのサイズ変更時にリサイズを避けるべきかを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) BOOL _shouldAvoidResizingWhenInputViewBoundsChange;
```

## Default Value
`_focusedElementInformation.shouldAvoidResizingWhenInputViewBoundsChange` を返す。

## Discussion
フォーカス中の要素のヒント情報に基づく単純な getter。

## References
- [`WKContentViewInteraction.h#L941`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L941)
- [`WKContentViewInteraction.mm#L10218`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L10218)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
