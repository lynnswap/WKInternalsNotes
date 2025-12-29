# ``WKInternalsNotes/WKActionSheetAssistant/showLinkSheet()``

リンク用のアクションシートを構築して表示する。

## Objective-C Declaration
```objective-c
- (void)showLinkSheet;
```

## Discussion
デリゲートから位置情報を取得してリンクURLを作成し、カスタムシートの有無を確認した上で既定アクションを構築する。デリゲートに最終アクションを決めてもらい、内容があればシートを生成・表示する。

## References
- [`WKActionSheetAssistant.h#L113`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKActionSheetAssistant.h#L113)
- [`WKActionSheetAssistant.mm#L641`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKActionSheetAssistant.mm#L641)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
