# ``WKInternalsNotes/WKContentView/inputLabelText()``

フォーカス中の入力要素に紐づくラベル文字列を返す。

## Objective-C Declaration
```objective-c
- (NSString *)inputLabelText;
```

## Discussion
`_focusedElementInformation` の `label` / `ariaLabel` / `title` / `placeholder` の順に返す。watchOS では placeholder が空の場合に input 種別に応じたフォールバック文言を返す。

## References
- [`WKContentViewInteraction.h#L865`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L865)
- [`WKContentViewInteraction.mm#L9878`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L9878)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
