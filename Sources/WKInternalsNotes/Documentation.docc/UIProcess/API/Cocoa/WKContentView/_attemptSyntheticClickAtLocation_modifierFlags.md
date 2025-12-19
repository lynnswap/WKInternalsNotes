# ``WKInternalsNotes/WKContentView/_attemptSyntheticClickAtLocation(_:modifierFlags:)``

合成クリックを WebPage に送る。

## Objective-C Declaration
```objective-c
- (void)_attemptSyntheticClickAtLocation:(CGPoint)location modifierFlags:(UIKeyModifierFlags)modifierFlags;
```

## Discussion
first responder でなければ `becomeFirstResponder` し、入力周辺機器の編集を終了してから `_page->attemptSyntheticClick` を呼び出す。呼び出し時には `_layerTreeTransactionIdAtLastInteractionStart` を使用する。

## References
- [WKContentViewInteraction.h#L822](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L822)
- [WKContentViewInteraction.mm#L4091](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L4091)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
