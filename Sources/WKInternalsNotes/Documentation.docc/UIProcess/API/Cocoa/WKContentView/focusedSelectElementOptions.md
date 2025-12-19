# ``WKInternalsNotes/WKContentView/focusedSelectElementOptions()``

フォーカス中の select 要素の option 配列を返す。

## Objective-C Declaration
```objective-c
- (Vector<WebKit::OptionItem>&) focusedSelectElementOptions;
```

## Discussion
`_focusedElementInformation.selectOptions` をそのまま返す。

## References
- [`WKContentViewInteraction.h#L841`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L841)
- [`WKContentViewInteraction.mm#L8215`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L8215)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
