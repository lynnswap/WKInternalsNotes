# ``WKInternalsNotes/WKActionSheetAssistant/handleElementActionWithType(_:element:needsInteraction:)``

要素アクションの種類に応じてデリゲート処理を振り分ける。

## Objective-C Declaration
```objective-c
- (void)handleElementActionWithType:(_WKElementActionType)type element:(_WKActivatedElementInfo *)element needsInteraction:(BOOL)needsInteraction;
```

## Discussion
`needsInteraction` が真の場合は開始/終了のデリゲートを通知する。`type` ごとにコピー/共有/保存/開く/画像解析/アニメーション制御などのアクションをデリゲートへ委譲し、共有はデータURLと画像有無に応じて画像共有またはURL共有を選ぶ。

## References
- [`WKActionSheetAssistant.h#L125`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKActionSheetAssistant.h#L125)
- [`WKActionSheetAssistant.mm#L1037`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKActionSheetAssistant.mm#L1037)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
