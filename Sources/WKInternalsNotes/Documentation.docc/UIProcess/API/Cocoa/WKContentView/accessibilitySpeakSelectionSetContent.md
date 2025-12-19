# ``WKInternalsNotes/WKContentView/accessibilitySpeakSelectionSetContent(_:)``

Speak Selection 用の文字列を受け取る。

## Objective-C Declaration
```objective-c
- (void)accessibilitySpeakSelectionSetContent:(NSString *)string;
```

## Discussion
`accessibilityRetrieveSpeakSelectionContent` が取得した文字列を通知するためのコールバックとして呼ばれる。

## References
- [`WKContentViewInteraction.mm#L1142`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L1142)
- [`WKContentViewInteraction.mm#L5071`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L5071)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
