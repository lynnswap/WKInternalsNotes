# ``WKInternalsNotes/WKContentView/focusedElementInformation``

フォーカス中要素の情報を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) const WebKit::FocusedElementInformation& focusedElementInformation;
```

## Default Value
`_focusedElementInformation` を返す。

## Discussion
内部で保持している `FocusedElementInformation` への参照を返す。

## References
- [`WKContentViewInteraction.h#L512`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L512)
- [`WKContentViewInteraction.mm#L8210`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L8210)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
