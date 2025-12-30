# ``WKInternalsNotes/WKActionSheetAssistantDelegate/actionSheetAssistant(_:copySubject:sourceMIMEType:)``

被写体コピーを実行する。

## Objective-C Declaration
```objective-c
- (void)actionSheetAssistant:(WKActionSheetAssistant *)assistant copySubject:(UIImage *)image sourceMIMEType:(NSString *)sourceMIMEType;
```

## Discussion
`copySubjectResultForImageContextMenu` が無い場合は何もしない。存在する場合は `imageDataForRemoveBackground` でデータを作成し、`UIPasteboard` に MIME タイプ付きで書き込む。

## References
- [`WKActionSheetAssistant.h#L68`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKActionSheetAssistant.h#L68)
- [`WKContentViewInteraction.mm#L13327`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L13327)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
