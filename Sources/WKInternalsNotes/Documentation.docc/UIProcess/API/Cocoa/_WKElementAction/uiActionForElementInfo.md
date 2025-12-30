# ``WKInternalsNotes/_WKElementAction/uiActionForElementInfo(_:)``

`UIAction` に変換する。

## Objective-C Declaration
```objective-c
- (UIAction *)uiActionForElementInfo:(_WKActivatedElementInfo *)elementInfo;
```

## Discussion
種別に対応する画像と識別子を取得し、ハンドラ内で `runActionWithElementInfo:` を呼ぶ `UIAction` を生成する。`disabled` が `YES` の場合は `UIMenuElementAttributesDisabled` を付与する。

## References
- [`_WKElementAction.h#L76`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKElementAction.h#L76)
- [`_WKElementAction.mm#L428`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKElementAction.mm#L428)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
