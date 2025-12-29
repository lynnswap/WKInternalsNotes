# ``WKInternalsNotes/WKActionSheetAssistant/defaultActionsForImageSheet(_:)``

画像向けの既定アクション一覧を生成する。

## Objective-C Declaration
```objective-c
- (RetainPtr<NSArray<_WKElementAction *>>)defaultActionsForImageSheet:(_WKActivatedElementInfo *)elementInfo;
```

## Discussion
`elementInfo` のURLに応じて「開く」「共有」などを追加し、Reading List対応や写真アクセス許可に応じて「リーディングリストに追加」「画像を保存」などを付与する。さらに画像解析/空間画像の可用性に応じたアクションとアニメーション操作を追加して返す。

## References
- [`WKActionSheetAssistant.h#L122`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKActionSheetAssistant.h#L122)
- [`WKActionSheetAssistant.mm#L594`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKActionSheetAssistant.mm#L594)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
