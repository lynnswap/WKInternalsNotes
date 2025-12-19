# ``WKInternalsNotes/WKContentView/_toolTipChanged(_:)``

ツールチップ文字列の更新を反映する。

## Objective-C Declaration
```objective-c
- (void)_toolTipChanged:(NSString *)newToolTip;
```

## Discussion
未作成なら `UIToolTipInteraction` を生成して追加し、`defaultToolTip` を更新して ToolTip マネージャに通知する。

## References
- [`WKContentViewInteraction.h#L888`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L888)
- [`WKContentViewInteraction.mm#L11525`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L11525)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
