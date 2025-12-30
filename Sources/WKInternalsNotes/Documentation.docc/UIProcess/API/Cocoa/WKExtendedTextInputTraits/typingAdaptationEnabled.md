# ``WKInternalsNotes/WKExtendedTextInputTraits/typingAdaptationEnabled``

タイピング適応が有効かどうかを示す。

## Objective-C Declaration
```objective-c
@property (nonatomic, getter=isTypingAdaptationEnabled) BOOL typingAdaptationEnabled;
```

## Default Value
初期値は `YES`。

## Discussion
`init` と `restoreDefaultValues` の両方で `YES` に設定される。

## References
- [`WKExtendedTextInputTraits.h#L52`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKExtendedTextInputTraits.h#L52)
- [`WKExtendedTextInputTraits.mm#L50`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKExtendedTextInputTraits.mm#L50)
- [`WKExtendedTextInputTraits.mm#L130`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKExtendedTextInputTraits.mm#L130)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
