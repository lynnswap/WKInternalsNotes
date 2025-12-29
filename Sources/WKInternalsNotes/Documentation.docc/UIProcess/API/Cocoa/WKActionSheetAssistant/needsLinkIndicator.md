# ``WKInternalsNotes/WKActionSheetAssistant/needsLinkIndicator``

リンクインジケータの表示が必要かを示す。

## Objective-C Declaration
```objective-c
@property (nonatomic) BOOL needsLinkIndicator;
```

## Default Value
`NO`（未設定）。

## Discussion
`_needsLinkIndicator` を返し、内部処理で `YES/NO` に更新される。

## References
- [`WKActionSheetAssistant.h#L111`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKActionSheetAssistant.h#L111)
- [`WKActionSheetAssistant.mm#L636`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKActionSheetAssistant.mm#L636)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
